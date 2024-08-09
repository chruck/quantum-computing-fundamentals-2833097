#!/bin/bash

##
# @file jupyter2py.sh
# @author Jas Eckard <jas+quantum@eckard.com>
#
# @section LICENSE
#
# GPL license
#
# @section DESCRIPTION
#
# This script strips out the python code from a Jupyter notebook and
# puts it into a python script.

# Return codes:  1 = bad parameter(s)
#                2 = required parameter missing
#                3 = notebookfile doesn't exist or is not readable

readonly localDir="$(pushd ${BASH_SOURCE[0]%/*} && pwd -P && popd >/dev/null)"

# To get some debug output call this file like:
# DEBUG=true ./jupyter2py.sh ...

echoStderr() { echo "$@" 1>&2; }

if [[ '' == "${DEBUG}" ]]; then
        # Make `debug' a no-op
        debug() { :; }
else
        debug() {
                echoStderr -n "DEBUG ${BASH_LINENO[*]}:  "
                echoStderr "$@"
        }
fi

# Usages:
#echo “regular stdout output”
#echoStderr “regular stderr output”
#debug “stderr output only seen when DEBUG set”

declare rc=0
declare optionA=0
#declare optionB=bogus
declare notebookfile
declare outputfilename
declare -a pythonOutput
readonly pi="3.1415"

Usage()
{
        cat 1>&2 <<EOFUsage

Usage:  $0 [OPTION]... notebookfile [outputfilename]

  -a, --optionA         Description
#  -b, --optionB VAL     Desc that takes VAL
  -h, -?, --help        Display this help and exit

  If no 'outputfilename' given, file will be 'notebookfile.py'.

EOFUsage
        exit ${rc}
}  # Usage()

parseOptions()
{
        debug "Original args:  $*"

        local shortopts="h?" ; local longopts="help,"
        shortopts+="a"; longopts+="optionA,"
#        shortopts+="b:"; longopts+="optionB:,"

        debug "shortopts=${shortopts} longopts=${longopts}"

        ARGS=$(getopt -o "${shortopts}" -l "${longopts}" -n "getopt.sh" -- "$@")

        getoptRc=$?
        if [[ 0 -ne "${getoptRc}" ]]; then
                echoStderr "ERROR:  getopt called incorrectly, rc=${getoptRc}"
                rc=1
                exit ${rc}
                # Alternatively, ($rc gets passed):
                #Usage
        fi

        eval set -- "${ARGS}"

        while true; do
                param=$1
                case "${param}" in
                        -a|--optionA)
                                debug "-a used"
                                optionA=1
                                shift
                                ;;
#                        -b|--optionB)
#                                shift
#                                if [[ -n "$1" ]]; then
#                                        debug "-b used: $1";
#                                        optionB=$1
#                                        shift;
#                                fi
#                                ;;
                        -h|-\?|--help)
                                debug "Asked for help"
                                Usage
                                ;;
                        --)
                                shift;
                                break;
                                ;;
                        *)
                                echoStderr "ERROR:  Unimplemented option: ${param}"
                                break;
                                ;;
                esac
        done

        debug "New args:  $*"

        # For 1 required and one optional argument
        if [[ 1 != "${#@}" && 2 != "${#@}" ]]; then
                rc=2
                echoStderr "ERROR:  notebookfile required."
        fi

        notebookfile=$1

        outputfilename="${notebookfile}.py"
        if [[ "$2" ]]; then
                outputfilename="$2"
        fi

#        if [[ 'bogus' == "${optionB}" ]]; then
#                rc=2
#                echoStderr "ERROR:  --optionB field required."
#        fi

        if [[ 0 != "${rc}" ]]; then
                Usage
        fi
}  # parseOptions()

# TODO:  Verify the parameters passed are valid
verifyParams()
{
#       if [[ "${optionB}" =~ /reg[ex]/ ]]; then
#               echoStderr "ERROR:  --optionB should be of the form: reg[ex]"
#               rc=2
#       fi

        if [[ ! -r "${notebookfile}" ]]; then
                echoStderr "ERROR:  notebookfile doesn't exist or" \
                       "is not readable"
                exit 3
        fi
}  # verifyParams()

#        while read line; do
#                echoStderr "WARNING:  I do not like ${line}"
#        done < <(grep "^${softwarebom}" ${steutabFName})

extractPython()
{
        pythonOutput=$(jq '.cells[].source[]' <"${notebookfile}")
}  # extractPython()

cleanExtractedPython()
{
        for line in ${pythonOutput}
        do
                :
        done
}  # cleanExtractedPython()

writeToFile()
{
        echo "${pythonOutput[@]}" | \
                sed 's/^"//;s/\\n"$//;s/"$//;s/^%/#%/;s/\\\\/\\/g;s/\\"/"/g' \
                >"${outputfilename}"
}  # writeToFile()

parseOptions "$@"
verifyParams
extractPython
#cleanExtractedPython
writeToFile

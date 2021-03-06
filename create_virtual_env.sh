#!/bin/bash

#===============================================================================
#
#          FILE:  create_virtual_env.sh
#
#         USAGE:  ./create_virtual_env.sh [OPTIONAL:VIRTUAL_ENVIRONMENT_NAME]
#
#   DESCRIPTION: As a helper this script creates the virtual environment for your project
#
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Ricardo Sarto, ricardo.soares.sarto@gmail.com
#       VERSION:  1.0
#       CREATED:  05/06/2021 18:51 PM GMT-3
#      REVISION:  ---
#===============================================================================

VIRTUAL_ENVIRONMENT_NAME=$1
echo "virtual environment name: $VIRTUAL_ENVIRONMENT_NAME"
if [ -z "${VIRTUAL_ENVIRONMENT_NAME}" ]; then
  echo $PWD
  VIRTUAL_ENVIRONMENT_NAME="venv_$(basename $PWD)"
fi
echo "about to create the virtual environment: $VIRTUAL_ENVIRONMENT_NAME"
APT_SEARCH_RESULT=$(apt-cache search '^python.*-venv' | grep '^python.*-venv' | sort | uniq -c | wc -l)
echo "found modules: $APT_SEARCH_RESULT"
if ["$APT_SEARCH_RESULT"="0"]; then
  echo "about to install python3-venv"
  sudo apt install python3-venv
fi
VENV_ABSOLUTE_PATH=$PWD/$VIRTUAL_ENVIRONMENT_NAME
echo "about to create the virtual environment: $VENV_ABSOLUTE_PATH"
python3 -m venv $VENV_ABSOLUTE_PATH
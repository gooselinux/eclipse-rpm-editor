#!/bin/sh
name=specfile-editor
svn_repo="svn://dev.eclipse.org/svnroot/technology/org.eclipse.linuxtools/rpm/tags/"

# Usage message
usage="usage: $0 <tag_name> <version_number>"
tag=$1
version_number=$2
tar_name=$name-fetched-src-$version_number

# Ensure we got the desired CVS tag
if [ "x$tag"x = "xx" ]
then
   echo >&2 "$usage"
   exit 1
fi

# cleanup dir
rm -fr $tar_name
# prepare archive
svn export $svn_repo/$tag $tar_name
# create archive
tar -cjf $tar_name.tar.bz2 $tar_name


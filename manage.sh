#!/bin/sh

# DATA
src_dir="src"

# COLORS
GREEN='\033[0;32m'
YELLO='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'


run(){
    echo "${GREEN}Starting server${NC}"
    python $src_dir/manage.py runserver
}

migrate(){
    if [ -n "$1" ]; then 
        echo "${GREEN}AVVIO migrazione${NC} (App $1)"
        python $src_dir/manage.py migrate $1
    else
        echo "${GREEN}AVVIO migrazione${NC} (GENERALE)"
        python $src_dir/manage.py migrate
    fi
}

compile_db(){
    if [ -n "$1" ]; then 
        echo "${GREEN}CREO migrazione${NC} (App $1)"
        python $src_dir/manage.py makemigrations $1
    else
        echo "${GREEN}CREO migrazione${NC} (GENERALE)"
        python $src_dir/manage.py makemigrations
    fi
}

delete(){
    echo "${RED}Cancello${NC} $1"
    find . -type d -name $1 -prune -exec rm -rf {} \; 2>/dev/null
}

case $1 in
    "run")
        run
    ;;
    "migrate")
        compile_db $2
        migrate $2
    ;;
    "full")
        delete migrations
        delete __pycache__

        echo "${RED}Cancello${NC} db.sqlite3"
        rm $src_dir/db.sqlite3 2>/dev/null

        compile_db $2
        migrate $2
        run
    ;;
    "clean")
        delete migrations
        delete __pycache__

        echo "${RED}Cancello${NC} db.sqlite3"
        rm $src_dir/db.sqlite3 2>/dev/null
    ;;
esac
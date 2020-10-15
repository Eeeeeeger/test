#!/bin/sh

get_current_time() {
    #echo "input parameter1: "$1" \n" 
    date --date='now' +%Y%m%d-%H:%M:%S
}
#get_current_time 1
#ct=$(get_current_time 1)
#echo $ct

get_today() {
  date --date='now' +%Y%m%d
}

get_formal_yesterday() {
  date --date="1 day ago" +%Y%m%d
}

get_trade_yesterday() {
  calendar_list=/data/raw/WIND/ASHARECALENDAR.txt
  today=$(get_today)
  awk -v today="$today" '{if($1<today) print $1}' "$calendar_list" | tail -n 1
}

is_trade_date() {
  query_date=$1
  calendar_list=/data/raw/WIND/ASHARECALENDAR.txt
  grep -c "$query_date" "$calendar_list"
}

 # just use as an example
get_cur_dir_path() {
  res=$(
    cd $(dirname "$0") || exit
    pwd
  )
  echo "$res"
}

echo "[$today] [TIME] $(get_current_time) [START]"


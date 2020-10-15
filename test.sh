#! /bin/bash
echo "hello world";
for file in $(ls /home/yigewang); do
    echo $file
done;
x='you are well done';
#echo $x;
#unset x;
#echo $x;
greeting="hello, "$x" !";
greeting_1="hello, ${x} !";
echo ${#x};
echo ${x:0:5};

echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";

echo "参数个数为：$#";
echo "传递的参数作为一个字符串显示：$*";

a=10
b=20

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a \* $b`
echo "a * b : $val"
#mutlti must add \ before *

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

if [ $a == $b ]
then
   echo "a 等于 b"
fi
if [ $a != $b ]
then
   echo "a 不等于 b"
fi

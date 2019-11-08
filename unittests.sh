conda install pycodestyle

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test1 python test_binary_tree.py
assert_no_stdout

run test2 pycodestyle test_binary_tree.py
assert_no_stdout
assert_no_stderr

run test3 python insert_key_value_pairs.py​ --data_struc hash --data rand.txt --entries 1000
assert_stdout
assert_no_stderr
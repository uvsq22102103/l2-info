from subprocess import Popen, PIPE

path = "./IN405/TD5/example1.sh"
process = Popen(path,stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
stdout = stdout.decode("utf-8") # format b'' vers str.
stderr = stderr.decode("utf-8") # idem
print(stdout+stderr)
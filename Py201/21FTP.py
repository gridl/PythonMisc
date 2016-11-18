import ftplib
from ftplib import FTP
ftp = FTP('ftp.debian.org')
ftp.login()
ftp.retrlines('LIST')
ftp.cwd('debian')
with open(out, 'wb') as f:
    ftp.retrbinary(('RETR ' + 'README.html', f.write)

# Downloading files
import os
ftp = ftplib.FTP('ftp.debian.org')
ftp.login()
ftp.cwd('debian')
filenames = ftp.nlst(()
for filename in filenames:
    host_file = os.path.join('/home/user/Desktop.test', filename)
    try:
        with open(host_file, 'wb') as local_file:
            ftp.retrbinary('RETR ' + filename, local_file.write)
        except ftplib.error_perm:
        pass
ftp.quit()


# Uploading files

def ftp_upload(ftp_obj, path, ftype='TXT'):
    if ftype == 'TXT':
        with open(path) as fobj:
            ftp.storlines('STOR ' + path, fobj)
        else:
            with open(path,'rb') as fobj:
                ftp.storbinary('STOR ' + path, fobj, 1024)

if __name__ == '__main__':
    ftp = ftplib.FTP('host', 'username', 'password')
    ftp.login()
    path = '/path/to/ksomething.pdf'
    ftp_upload(ftp, pdf_path, ftype='PDF')
    ftp.quit()

# Install openssh-server inside the container
RUN apt-get update \
 && apt-get install -y \
    openssh-server \
 && apt-get clean
RUN echo \
    "ChallengeResponseAuthentication no\n" \
    "UsePAM yes\n" \
    "X11Forwarding yes\n" \
    "PrintMotd no\n" \
    "AcceptEnv *\n" \
    "Subsystem sftp /usr/lib/openssh/sftp-server\n" \
    > /etc/ssh/sshd_config
RUN mkdir -p /run/sshd

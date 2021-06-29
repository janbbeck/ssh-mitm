import logging
import time
import re

from paramiko.common import cMSG_CHANNEL_REQUEST, cMSG_CHANNEL_CLOSE, cMSG_CHANNEL_EOF
from paramiko.message import Message

from ssh_proxy_server.forwarders.base import BaseForwarder


class X11BaseForwarder(BaseForwarder):

    def forward(self):
        if self.session.ssh_pty_kwargs is not None:
            self.server_channel.get_pty(**self.session.ssh_pty_kwargs)

        logging.info(self.server_channel.request_x11(
            screen_number=self.session.x11_screen_number, 
            auth_protocol=self.session.x11_auth_protocol, 
            auth_cookie=self.session.x11_auth_cookie, 
            single_connection=self.session.x11_single_connection, 
            handler=None
        ))

        try:
            while self.session.running:
                # redirect stdout <-> stdin und stderr <-> stderr
                if self.session.x11_channel.recv_ready():
                    buf = self.session.x11_channel.recv(self.BUF_LEN)
                    self.session.server_channel.sendall(buf)
                if self.server_channel.recv_ready():
                    buf = self.server_channel.recv(self.BUF_LEN)
                    self.session.x11_channel.sendall(buf)
                time.sleep(0.1)
        except Exception:
            logging.exception('error processing scp command')
            raise


class X11Forwarder(X11BaseForwarder):
    pass

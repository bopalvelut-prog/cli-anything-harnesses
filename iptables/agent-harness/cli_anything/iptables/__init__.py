import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def rules(): subprocess.run(['iptables', '-L', '-n'])
@cli.command()
@click.argument('port')
def allow(port): subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', port, '-j', 'ACCEPT'])
@cli.command()
@click.argument('port')
def block(port): subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', port, '-j', 'DROP'])
if __name__ == '__main__': cli()

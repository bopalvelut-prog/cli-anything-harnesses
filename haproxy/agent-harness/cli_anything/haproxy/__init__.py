import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def reload(): subprocess.run(['haproxy', '-f', '/etc/haproxy/haproxy.cfg', '-st', '$(cat /run/haproxy.pid)'])
@cli.command()
@click.argument('config')
def test(config): subprocess.run(['haproxy', '-c', '-f', config])
if __name__ == '__main__': cli()

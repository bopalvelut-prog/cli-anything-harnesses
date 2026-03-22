import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def version(): subprocess.run(['openssl', 'version'])
@cli.command()
@click.argument('domain')
@click.option('--port', default=443)
def check(domain, port): subprocess.run(['openssl', 's_client', '-connect', f'{domain}:{port}'])
@cli.command()
@click.argument('keyfile')
def genkey(keyfile): subprocess.run(['openssl', 'req', '-new', '-newkey', 'rsa:2048', '-nodes', '-keyout', keyfile])
if __name__ == '__main__': cli()

import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('domain')
def obtain(domain): subprocess.run(['certbot', 'certonly', '--standalone', '-d', domain])
@cli.command()
def renew(): subprocess.run(['certbot', 'renew'])
@cli.command()
@click.argument('domain')
def revoke(domain): subprocess.run(['certbot', 'revoke', '-d', domain])
if __name__ == '__main__': cli()

import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('domain')
def renew(domain): subprocess.run(['letsencrypt', 'renew', '--cert-name', domain])
if __name__ == '__main__': cli()

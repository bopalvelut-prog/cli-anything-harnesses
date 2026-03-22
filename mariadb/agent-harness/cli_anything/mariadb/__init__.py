import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('MariaDB running')
@cli.command()
@click.argument('query')
def query(query): subprocess.run(['mysql', '-e', query])
@cli.command()
def restart(): subprocess.run(['systemctl', 'restart', 'mariadb'])
if __name__ == '__main__': cli()

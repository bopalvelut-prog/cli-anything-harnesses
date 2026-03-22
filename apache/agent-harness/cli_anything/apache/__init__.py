
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Apache status')
@cli.command()
@click.argument('config')
def test(config): subprocess.run(['apachectl', '-t', '-f', config])
if __name__ == '__main__': cli()

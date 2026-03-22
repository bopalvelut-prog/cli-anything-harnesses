import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def audit(): click.echo('Gatekeeper audit')
@cli.command()
def status(): click.echo('Gatekeeper status')
if __name__ == '__main__': cli()

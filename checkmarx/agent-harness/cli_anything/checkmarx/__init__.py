import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('Checkmarx scan')
@cli.command()
def status(): click.echo('Checkmarx status')
if __name__ == '__main__': cli()

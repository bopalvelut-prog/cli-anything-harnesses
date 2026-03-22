import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def scan(): click.echo('Wiz scan')
@cli.command()
def issues(): click.echo('Wiz issues')
if __name__ == '__main__': cli()

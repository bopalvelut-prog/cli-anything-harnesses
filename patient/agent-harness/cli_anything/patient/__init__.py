import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('patient running')
@cli.command()
def start(): click.echo('patient started')
if __name__ == '__main__': cli()

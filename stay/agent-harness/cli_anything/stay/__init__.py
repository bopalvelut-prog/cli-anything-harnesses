import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stay running')
@cli.command()
def start(): click.echo('stay started')
if __name__ == '__main__': cli()

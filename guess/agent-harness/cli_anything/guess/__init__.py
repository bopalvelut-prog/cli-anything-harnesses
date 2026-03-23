import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('guess running')
@cli.command()
def start(): click.echo('guess started')
if __name__ == '__main__': cli()

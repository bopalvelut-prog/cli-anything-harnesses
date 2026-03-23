import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blueman running')
@cli.command()
def start(): click.echo('blueman started')
if __name__ == '__main__': cli()

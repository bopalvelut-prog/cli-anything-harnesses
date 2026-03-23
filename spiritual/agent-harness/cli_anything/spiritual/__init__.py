import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spiritual running')
@cli.command()
def start(): click.echo('spiritual started')
if __name__ == '__main__': cli()

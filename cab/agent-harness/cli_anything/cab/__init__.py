import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cab running')
@cli.command()
def start(): click.echo('cab started')
if __name__ == '__main__': cli()

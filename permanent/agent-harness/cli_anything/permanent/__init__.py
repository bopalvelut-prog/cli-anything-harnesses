import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('permanent running')
@cli.command()
def start(): click.echo('permanent started')
if __name__ == '__main__': cli()

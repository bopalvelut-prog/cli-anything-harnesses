import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('haiku running')
@cli.command()
def start(): click.echo('haiku started')
if __name__ == '__main__': cli()

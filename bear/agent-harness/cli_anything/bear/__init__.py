import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bear running')
@cli.command()
def start(): click.echo('bear started')
if __name__ == '__main__': cli()

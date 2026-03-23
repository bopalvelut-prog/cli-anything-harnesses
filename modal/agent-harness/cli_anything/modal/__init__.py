import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('modal running')
@cli.command()
def start(): click.echo('modal started')
if __name__ == '__main__': cli()

import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('response running')
@cli.command()
def start(): click.echo('response started')
if __name__ == '__main__': cli()

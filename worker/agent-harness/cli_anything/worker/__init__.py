import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('worker running')
@cli.command()
def start(): click.echo('worker started')
if __name__ == '__main__': cli()

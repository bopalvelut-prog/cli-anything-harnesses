import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('daisy running')
@cli.command()
def start(): click.echo('daisy started')
if __name__ == '__main__': cli()

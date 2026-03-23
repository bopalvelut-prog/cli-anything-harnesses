import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pegasus running')
@cli.command()
def start(): click.echo('pegasus started')
if __name__ == '__main__': cli()

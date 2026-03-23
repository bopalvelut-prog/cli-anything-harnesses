import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kinesis running')
@cli.command()
def start(): click.echo('kinesis started')
if __name__ == '__main__': cli()

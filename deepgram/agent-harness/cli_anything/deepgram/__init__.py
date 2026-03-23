import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deepgram running')
@cli.command()
def start(): click.echo('deepgram started')
if __name__ == '__main__': cli()

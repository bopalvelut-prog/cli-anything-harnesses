import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('asr running')
@cli.command()
def start(): click.echo('asr started')
if __name__ == '__main__': cli()

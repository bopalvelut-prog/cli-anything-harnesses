import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('snort running')
@cli.command()
def start(): click.echo('snort started')
if __name__ == '__main__': cli()

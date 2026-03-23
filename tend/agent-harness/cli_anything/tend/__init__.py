import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tend running')
@cli.command()
def start(): click.echo('tend started')
if __name__ == '__main__': cli()

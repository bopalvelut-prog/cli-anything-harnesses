import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('checkmk running')
@cli.command()
def start(): click.echo('checkmk started')
if __name__ == '__main__': cli()

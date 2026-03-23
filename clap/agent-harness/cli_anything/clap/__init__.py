import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clap running')
@cli.command()
def start(): click.echo('clap started')
if __name__ == '__main__': cli()

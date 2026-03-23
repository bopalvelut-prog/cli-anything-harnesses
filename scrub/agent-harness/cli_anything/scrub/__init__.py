import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scrub running')
@cli.command()
def start(): click.echo('scrub started')
if __name__ == '__main__': cli()

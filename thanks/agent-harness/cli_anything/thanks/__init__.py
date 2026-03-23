import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thanks running')
@cli.command()
def start(): click.echo('thanks started')
if __name__ == '__main__': cli()

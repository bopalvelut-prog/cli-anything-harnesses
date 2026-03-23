import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rep running')
@cli.command()
def start(): click.echo('rep started')
if __name__ == '__main__': cli()

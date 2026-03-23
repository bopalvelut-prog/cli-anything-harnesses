import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('optaplanner running')
@cli.command()
def start(): click.echo('optaplanner started')
if __name__ == '__main__': cli()

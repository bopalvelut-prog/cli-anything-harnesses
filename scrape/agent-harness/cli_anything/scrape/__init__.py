import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scrape running')
@cli.command()
def start(): click.echo('scrape started')
if __name__ == '__main__': cli()

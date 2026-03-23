import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bulk_extractor running')
@cli.command()
def start(): click.echo('bulk_extractor started')
if __name__ == '__main__': cli()

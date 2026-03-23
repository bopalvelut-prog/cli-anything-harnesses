import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bam running')
@cli.command()
def start(): click.echo('bam started')
if __name__ == '__main__': cli()

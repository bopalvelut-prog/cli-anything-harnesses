import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ActivityWatch running')
@cli.command()
def buckets(): click.echo('ActivityWatch buckets')
if __name__ == '__main__': cli()

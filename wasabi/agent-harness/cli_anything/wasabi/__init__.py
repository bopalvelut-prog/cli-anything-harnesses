import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Wasabi status')
@cli.command()
def buckets(): click.echo('Wasabi buckets')
if __name__ == '__main__': cli()

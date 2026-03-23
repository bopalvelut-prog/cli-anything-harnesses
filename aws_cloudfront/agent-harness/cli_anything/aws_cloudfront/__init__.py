import click
@click.group()
def cli(): pass
@cli.command()
def invalidate(): click.echo('CloudFront invalidate')
@cli.command()
def distributions(): click.echo('CloudFront distributions')
if __name__ == '__main__': cli()

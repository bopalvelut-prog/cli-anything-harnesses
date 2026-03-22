import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['mdadm', '--detail', '/dev/md0'])
@cli.command()
def create(): click.echo('Creating RAID array')
if __name__ == '__main__': cli()

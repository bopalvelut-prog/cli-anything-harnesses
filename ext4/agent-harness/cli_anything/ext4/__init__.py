import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def check(): subprocess.run(['e2fsck', '-n', '/dev/sda1'])
@cli.command()
def resize(): click.echo('Resizing ext4')
if __name__ == '__main__': cli()
